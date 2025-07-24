import pytest
from unittest.mock import Mock, patch
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from datetime import datetime, timedelta
import jwt
import os
from api.security import (
    create_jwt_token, 
    verify_jwt_token, 
    verify_token,
    SECRET_KEY,
    ALGORITHM
)


class TestJWTSecurity:
    """Test cases for JWT security functions"""
    
    def test_create_jwt_token_default_expiry(self):
        """Test JWT token creation with default expiry"""
        data = {"sub": "testuser", "role": "admin"}
        token = create_jwt_token(data)
        
        assert isinstance(token, str)
        assert len(token) > 0
        
        # Decode and verify the token
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert decoded["sub"] == "testuser"
        assert decoded["role"] == "admin"
        assert "exp" in decoded
    
    
    def test_verify_jwt_token_valid(self):
        """Test JWT token verification with valid token"""
        data = {"sub": "testuser", "role": "user"}
        token = create_jwt_token(data)
        
        payload = verify_jwt_token(token)
        assert payload["sub"] == "testuser"
        assert payload["role"] == "user"
    
    def test_verify_jwt_token_expired(self):
        """Test JWT token verification with expired token"""
        data = {"sub": "testuser"}
        expired_token = create_jwt_token(data, expires_delta=timedelta(seconds=-10))
        
        with pytest.raises(HTTPException) as exc_info:
            verify_jwt_token(expired_token)
        
        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Token expired"
    
    def test_verify_jwt_token_invalid_signature(self):
        """Test JWT token verification with invalid signature"""
        # Create token with wrong secret
        data = {"sub": "testuser"}
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(hours=1)
        to_encode.update({"exp": expire})
        invalid_token = jwt.encode(to_encode, "wrong_secret", algorithm=ALGORITHM)
        
        with pytest.raises(HTTPException) as exc_info:
            verify_jwt_token(invalid_token)
        
        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Invalid token"
    
    def test_verify_jwt_token_malformed(self):
        """Test JWT token verification with malformed token"""
        malformed_token = "not.a.jwt.token"
        
        with pytest.raises(HTTPException) as exc_info:
            verify_jwt_token(malformed_token)
        
        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Invalid token"
    
    def test_verify_jwt_token_empty(self):
        """Test JWT token verification with empty token"""
        with pytest.raises(HTTPException) as exc_info:
            verify_jwt_token("")
        
        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Invalid token"
    
    @pytest.mark.asyncio
    async def test_verify_token_function_valid(self):
        """Test verify_token function with valid credentials"""
        data = {"sub": "testuser"}
        token = create_jwt_token(data)
        
        # Mock HTTPAuthorizationCredentials
        credentials = Mock()
        credentials.credentials = token
        
        result = await verify_token(credentials)
        assert result["sub"] == "testuser"
    
    @pytest.mark.asyncio
    async def test_verify_token_function_invalid(self):
        """Test verify_token function with invalid credentials"""
        # Mock HTTPAuthorizationCredentials with invalid token
        credentials = Mock()
        credentials.credentials = "invalid.token.here"
        
        with pytest.raises(HTTPException) as exc_info:
            await verify_token(credentials)
        
        assert exc_info.value.status_code == 401
        assert exc_info.value.detail == "Invalid token"


class TestSecurityConfiguration:
    """Test cases for security configuration"""
    
    def test_secret_key_environment_variable(self):
        """Test that SECRET_KEY can be set via environment variable"""
        with patch.dict(os.environ, {"SECRET_KEY": "test_secret_key"}):
            # Import module again to get new environment variable
            import importlib
            from api import security
            importlib.reload(security)
            
            # Verify the secret key is read from environment
            assert security.SECRET_KEY == "test_secret_key"
    
    def test_algorithm_environment_variable(self):
        """Test that ALGORITHM can be set via environment variable"""
        with patch.dict(os.environ, {"ALGORITHM": "HS512"}):
            # Import module again to get new environment variable
            import importlib
            from api import security
            importlib.reload(security)
            
            # Verify the algorithm is read from environment
            assert security.ALGORITHM == "HS512"
    
    def test_default_secret_key(self):
        """Test default secret key when environment variable is not set"""
        with patch.dict(os.environ, {}, clear=True):
            # Import module again to get default values
            import importlib
            from api import security
            importlib.reload(security)
            
            # Verify default secret key is used
            assert security.SECRET_KEY == "v3ryS3cr3tAndRand0mK3y!1234567890"
    
    def test_default_algorithm(self):
        """Test default algorithm when environment variable is not set"""
        with patch.dict(os.environ, {}, clear=True):
            # Import module again to get default values
            import importlib
            from api import security
            importlib.reload(security)
            
            # Verify default algorithm is used
            assert security.ALGORITHM == "HS256"


class TestTokenEdgeCases:
    """Test edge cases for token handling"""
    
    def test_token_with_special_characters_in_payload(self):
        """Test token creation and verification with special characters in payload"""
        data = {"sub": "user@example.com", "name": "José María", "role": "admin"}
        token = create_jwt_token(data)
        
        payload = verify_jwt_token(token)
        assert payload["sub"] == "user@example.com"
        assert payload["name"] == "José María"
        assert payload["role"] == "admin"
    
    def test_token_with_empty_payload(self):
        """Test token creation and verification with minimal payload"""
        data = {}
        token = create_jwt_token(data)
        
        payload = verify_jwt_token(token)
        assert "exp" in payload  # Expiry should always be present
    
    def test_token_with_large_payload(self):
        """Test token creation and verification with large payload"""
        data = {
            "sub": "testuser",
            "permissions": ["read", "write", "delete"] * 100,  # Large list
            "metadata": {"key" + str(i): "value" + str(i) for i in range(50)}  # Large dict
        }
        token = create_jwt_token(data)
        
        payload = verify_jwt_token(token)
        assert payload["sub"] == "testuser"
        assert len(payload["permissions"]) == 300
        assert len(payload["metadata"]) == 50

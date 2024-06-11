import unittest
from unittest.mock import Mock, patch
from microservices.user_microservice.app.services.user_service import UserService

class TestUserService(unittest.TestCase):
    @patch('app.cache')
    @patch('app.repository.user_repository.UserRepository')
    def test_create(self, mock_repo, mock_cache):
        # Arrange
        test_user = Mock()
        test_user.id = 1
        mock_repo.create.return_value = test_user

        service = UserService(mock_repo)

        # Act
        result = service.create(test_user)

        # Assert
        mock_repo.create.assert_called_once_with(test_user)
        mock_cache.set.assert_called_once_with('user_1', test_user, timeout=50)
        self.assertEqual(result, test_user)

if __name__ == '__main__':
    unittest.main()
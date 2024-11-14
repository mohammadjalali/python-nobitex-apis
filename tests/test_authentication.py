import pytest

from nobitex.authentication import Authentication


@pytest.mark.skip(
    reason="Needs to set username and password and twofactor_authentication_code"
)
def test_generate_key():
    import nobitex.config as config

    # Arrange
    authentication = Authentication()
    username = config.USERNAME
    password = config.PASSWORD
    two_factor_authentication_code = config.TWO_FACTOR_AUTHENTICATION_CODE

    # Act
    key = authentication.generate_key(
        username, password, two_factor_authentication_code
    )

    # Assert
    assert key != ""

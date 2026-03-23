def test_profile_has_all_keys(fake):
    profile = fake.profile()
    expected_keys = {
        "name", "id_number", "email", "mobile", "landline", "address",
        "postal_code", "company", "job_title", "birthday", "credit_card",
        "bank_account", "username",
    }
    assert set(profile.keys()) == expected_keys


def test_profile_values_are_strings(fake):
    profile = fake.profile()
    for key, value in profile.items():
        assert isinstance(value, str), f"{key} is not a string: {type(value)}"

import re


def test_job_title_is_chinese(fake):
    for _ in range(20):
        title = fake.job_title()
        assert re.search(r"[\u4e00-\u9fff]", title), f"Not Chinese: {title}"
        assert len(title) >= 2

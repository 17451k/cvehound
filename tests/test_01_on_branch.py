#!/usr/bin/env python3

import pytest
from cvehound.exception import UnsupportedVersion

@pytest.mark.fast
@pytest.mark.notbackported(
    ('cve', 'branch'),
    [
        ('CVE-2019-12382', 'stable/linux-4.9.y'), # Disputed
        ('CVE-2020-27777', 'stable/linux-4.9.y'),
        ('CVE-2019-12455', 'stable/linux-4.9.y'), # Disputed
        ('CVE-2019-12455', 'stable/linux-4.14.y'), # Disputed
        ('CVE-2019-12455', 'stable/linux-4.19.y'), # Disputed
        ('CVE-2022-1011', 'stable/linux-4.9.y'),
        ('CVE-2022-0998', 'stable/linux-5.15.y'),
        ('CVE-2022-0812', 'stable/linux-4.19.y'),
        ('CVE-2022-0812', 'stable/linux-4.14.y'),
        ('CVE-2022-0812', 'stable/linux-4.9.y'),
        ('CVE-2022-1652', 'stable/linux-5.15.y'),
        ('CVE-2022-1652', 'stable/linux-5.10.y'),
        ('CVE-2022-1652', 'stable/linux-5.4.y'),
        ('CVE-2022-1652', 'stable/linux-4.19.y'),
        ('CVE-2022-1652', 'stable/linux-4.14.y'),
        ('CVE-2022-1652', 'stable/linux-4.9.y'),
        ('CVE-2021-3635', 'stable/linux-4.14.y'),
        ('CVE-2022-28388', 'stable/linux-4.9.y'),
        ('CVE-2022-1852', 'stable/linux-5.15.y'),
        ('CVE-2022-1852', 'stable/linux-5.10.y'),
        ('CVE-2022-1789', 'stable/linux-5.4.y'),
        ('CVE-2022-1789', 'stable/linux-4.19.y'),
        ('CVE-2021-28660', 'stable/linux-5.15.y'),
        ('CVE-2022-34918', 'stable/linux-5.4.y'),
        ('CVE-2022-34918', 'stable/linux-4.19.y'),
        ('CVE-2022-34918', 'stable/linux-4.14.y'),
        ('CVE-2022-34918', 'stable/linux-4.9.y'),
        ('CVE-2022-21505', 'stable/linux-5.15.y'),
        ('CVE-2022-21505', 'stable/linux-5.10.y'),
        ('CVE-2022-21505', 'stable/linux-5.4.y'),
    ]
)
def test_on_branch(hound, branch, cve):
    try:
        assert not hound.check_cve(cve), cve + ' on ' + branch
    except UnsupportedVersion:
        pytest.skip('Unsupported spatch version')

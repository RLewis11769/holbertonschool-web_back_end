# Unit tests and Integration Tests

## Description

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute tests with:
```
python -m unittest test_file.py
```

## Starter Files

- utils.py
- client.py
- fixtures.py

## Tasks


### 0
- Test for access_nested_map function
- Use parametrized.expand to test given inputs have expected outputs
    - Affected file:
        - test_utils.py
    - Based on:
        - utils.py

### 1
- Test for access_nested_map function
- Use parameterized.expand to test given incorrect inputs raise KeyError
    - Affected file:
        - test_utils.py
    - Based on:
        - utils.py

### 2
- Test for get_json function
- Use parameterized.expand with mock.patch to patch requests.get to return json payload return value for given url
    - Affected file:
        - test_utils.py
    - Based on:
        - utils.py

### 3
- Test for memoize decorator
- Define TestCase class with method/property that return given value
- Use mock.patch to mock TestCase's method - when called twice, method is only called once
    - Affected file:
        - test_utils.py
    - Based on:
        - utils.py

### 4
- Test for GithubOrgClient.org method
- Use parameterized.expand and patch decorator to test passing org_name returns expected dict
    - Affected file:
        - test_client.py
    - Based on:
        - client.py

### 5
- Test for GithubOrgClient._public_repos_url
- Use patch context manager and PropertyMock to test return value of key repos_url
    - Affected file:
        - test_client.py
    - Based on:
        - client.py

### 6
- Test for GithubOrgClient.public_repos
- Use patch decorator, patch context manager, and PropertyMock to test return value from given key
- Method uses _public_repos_url, org, and get_json
    - Affected file:
        - test_client.py
    - Based on:
        - client.py

### 7
- Test for GithubOrgClient.has_license
- Use parameterized.expand to to test that given inputs have expected values
    - Affected file:
        - test_client.py
    - Based on:
        - client.py

### 8
- Integration test for GithubOrgClient.public_repos
- Mock code that sends external requests
- Use parameterized_class and patcher to return example payload found in fixtures
- Write setUpClass and tearDownClass classmethods for TestCase API
    - Affected file:
        - test_client.py
    - Based on:
        - client.py
        - fixtures.py

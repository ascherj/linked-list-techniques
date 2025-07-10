#!/usr/bin/env python3
"""
Test runner for all linked list unit tests.
This script runs all test files and provides a comprehensive summary.
"""

import unittest
import sys
import os
from io import StringIO

# Add the parent directory to the path so we can import from src
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def run_test_file(test_module_name):
    """Run tests from a specific module and return results"""
    try:
        # Import the test module
        test_module = __import__(test_module_name)

        # Create a test suite
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_module)

        # Run the tests
        stream = StringIO()
        runner = unittest.TextTestRunner(stream=stream, verbosity=2)
        result = runner.run(suite)

        return {
            'module': test_module_name,
            'tests_run': result.testsRun,
            'failures': len(result.failures),
            'errors': len(result.errors),
            'success': result.wasSuccessful(),
            'output': stream.getvalue()
        }
    except Exception as e:
        return {
            'module': test_module_name,
            'tests_run': 0,
            'failures': 0,
            'errors': 1,
            'success': False,
            'output': f"Error importing {test_module_name}: {str(e)}"
        }

def main():
    """Run all tests and display summary"""
    print("=" * 60)
    print("LINKED LIST UNIT TESTS")
    print("=" * 60)

    # Test modules to run
    test_modules = [
        'test_linked_list_base',
        'test_multiple_pass',
        'test_slow_fast',
        'test_temporary_head'
    ]

    results = []
    total_tests = 0
    total_failures = 0
    total_errors = 0

    # Run each test module
    for module in test_modules:
        print(f"\n{'='*20} {module.upper()} {'='*20}")
        result = run_test_file(module)
        results.append(result)

        total_tests += result['tests_run']
        total_failures += result['failures']
        total_errors += result['errors']

        # Print individual test results
        if result['success']:
            print(f"✅ {result['tests_run']} tests passed")
        else:
            print(f"❌ {result['failures']} failures, {result['errors']} errors out of {result['tests_run']} tests")
            if result['output']:
                print("\nDetailed output:")
                print(result['output'])

    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    for result in results:
        status = "✅ PASS" if result['success'] else "❌ FAIL"
        print(f"{result['module']:<25} {status:>10} ({result['tests_run']} tests)")

    print(f"\nTotal Tests: {total_tests}")
    print(f"Total Failures: {total_failures}")
    print(f"Total Errors: {total_errors}")

    if total_failures == 0 and total_errors == 0:
        print("\n🎉 ALL TESTS PASSED! 🎉")
        return 0
    else:
        print(f"\n💥 {total_failures + total_errors} TEST(S) FAILED")
        return 1

if __name__ == '__main__':
    sys.exit(main())

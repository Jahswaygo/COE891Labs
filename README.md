# COE891 Labs - Software Testing and Quality Assurance

This repository contains the lab exercises for the **Software Testing and Quality Assurance** course. Each lab focuses on different aspects of software testing, including unit testing, parameterized testing, theory-based testing, code coverage analysis, advanced testing techniques, web application testing, and mutation testing. Below is a detailed explanation of each lab and the tests conducted.

---

## Lab 1: Introduction to Unit Testing and Parameterized Testing

### Overview
Lab 1 introduces the basics of unit testing using JUnit (Java) and `unittest` (Python). It covers parameterized testing, test suites, and the use of theories for testing mathematical and logical properties.

### Key Exercises

1. **Triangle Area Calculation**
   - **Objective**: Validate the area calculation of triangles with different side lengths.
   - **Tests**:
     - Verify the area of valid triangles (e.g., right triangles, isosceles triangles).
     - Ensure invalid triangles (e.g., sides that don't satisfy the triangle inequality) raise appropriate errors.
     - Compare the areas of triangles with the same dimensions but different side orders.

2. **Phone Number Validation**
   - **Objective**: Test regular expressions for validating phone numbers.
   - **Tests**:
     - Validate phone numbers with different formats (e.g., with/without spaces, parentheses).
     - Ensure invalid formats (e.g., letters in phone numbers) are rejected.

3. **Fibonacci Sequence**
   - **Objective**: Verify the correctness of Fibonacci sequence computation.
   - **Tests**:
     - Parameterized tests for various Fibonacci numbers (e.g., Fibonacci(0) = 0, Fibonacci(5) = 5).
     - Ensure edge cases like Fibonacci(0) and Fibonacci(1) are handled correctly.

4. **Prime Number Checker**
   - **Objective**: Test the `isPrime` method using parameterized tests.
   - **Tests**:
     - Verify prime and non-prime numbers (e.g., 2 is prime, 6 is not prime).
     - Use a collection of test cases to ensure robustness.

5. **Mathematical Theories**
   - **Objective**: Test mathematical properties like commutativity and sum comparisons.
   - **Tests**:
     - Theories to verify that the sum of two numbers is greater than each individual number.
     - Theories to validate the commutative property of addition.

---

## Lab 2: Code Coverage and Test Automation

### Overview
Lab 2 focuses on code coverage analysis using Clover and test automation with Ant build scripts.

### Key Exercises

1. **Clover Integration**
   - **Objective**: Instrument code with Clover to measure test coverage.
   - **Tests**:
     - Generate HTML reports to visualize coverage metrics.
     - Ensure all critical paths and edge cases are covered.
     - Analyze uncovered lines of code and improve test cases to achieve higher coverage.

2. **Ant Build Script**
   - **Objective**: Automate the build, test, and reporting process.
   - **Steps**:
     - Clean build directories.
     - Compile source and test code.
     - Run JUnit tests with Clover instrumentation.
     - Generate Clover coverage reports.
   - **Outcome**:
     - A fully automated build and test pipeline with integrated code coverage reporting.

---

## Lab 3: Advanced Testing Techniques and Web Application Testing

### Overview
Lab 3 explores advanced testing techniques, including **boundary value analysis**, **equivalence partitioning**, and **decision table testing**. Additionally, it introduces **web application testing** using Selenium for automated browser-based testing.

### Key Exercises

1. **Boundary Value Analysis**
   - **Objective**: Test edge cases for input ranges to ensure the system behaves correctly at the boundaries of valid and invalid inputs.
   - **Tests**:
     - Identify boundary values for input ranges (e.g., minimum, maximum, just inside, just outside).
     - Validate the system's behavior at these boundaries.

2. **Equivalence Partitioning**
   - **Objective**: Group inputs into equivalence classes and test representative values from each class to reduce the number of test cases while maintaining coverage.
   - **Tests**:
     - Divide input ranges into valid and invalid equivalence classes.
     - Test one representative value from each class.

3. **Decision Table Testing**
   - **Objective**: Use decision tables to test combinations of inputs and their corresponding outputs systematically.
   - **Tests**:
     - Create a decision table with all possible input combinations and expected outputs.
     - Verify the system's behavior for each combination.

4. **Web Application Testing with Selenium**
   - **Objective**: Automate testing of a web application using Selenium WebDriver.
   - **Tests**:
     - Verify the title of a web page.
     - Automate adding items to a to-do list and verify they appear correctly.
     - Automate marking items as completed and validate the UI updates.
     - Validate the number of completed items matches the expected value.

5. **Test Automation Framework**
   - **Objective**: Implement a basic test automation framework for Selenium tests.
   - **Features**:
     - Modular test scripts for reusability.
     - Setup and teardown methods for initializing and cleaning up test environments.
     - Assertions to validate test outcomes.

---

## Lab 4: Test Suites and Edge Coverage

### Overview
Lab 4 focuses on creating test suites and achieving edge coverage in control flow graphs.

### Key Exercises

1. **Test Suites**
   - **Objective**: Combine multiple test cases into a single suite for efficient execution.
   - **Tests**:
     - Ensure all test cases from different modules are executed together.
     - Validate the results of the combined test suite.

2. **Edge Coverage**
   - **Objective**: Achieve 100% edge coverage in control flow graphs.
   - **Tests**:
     - Design test cases to traverse all edges in the program's control flow.
     - Identify and test all decision points and branches.

3. **Prime Path Coverage**
   - **Objective**: Ensure all prime paths in the control flow graph are tested.
   - **Tests**:
     - Create test cases to cover all unique paths in the program.

---

## Lab 5: Mocking, Stubbing, and Predicate Coverage

### Overview
Lab 5 introduces mocking and stubbing techniques to isolate components during testing. It also explores predicate and clause coverage for logical expressions.

### Key Exercises

1. **Mocking External Dependencies**
   - **Objective**: Replace external dependencies with mock objects to isolate the system under test.
   - **Tests**:
     - Verify the behavior of components in isolation by mocking APIs, databases, or external services.

2. **Stubbing Methods**
   - **Objective**: Stub methods to return predefined values for testing.
   - **Tests**:
     - Replace complex or unreliable methods with stubs to simplify testing.

3. **Predicate and Clause Coverage**
   - **Objective**: Test logical expressions for all possible outcomes.
   - **Tests**:
     - **General Active Clause Coverage (GACC)**: Ensure each clause independently affects the predicate's outcome.
     - **Correlated Active Clause Coverage (CACC)**: Test combinations of clauses that affect the predicate.
     - **Restricted Active Clause Coverage (RACC)**: Test minimal combinations of clauses.

---

## Lab 6: Mutation Testing and Code Coverage Analysis

### Overview
Lab 6 focuses on **mutation testing** to evaluate the effectiveness of test cases and **code coverage analysis** to measure the extent of code execution during testing.

### Key Exercises

1. **Mutation Testing with `mutmut`**
   - **Objective**: Assess the quality of test cases by introducing mutations (small changes) into the code and verifying if the tests detect these changes.
   - **Steps**:
     - Run `mutmut run` to execute mutation testing.
     - Use `mutmut results` to view the results of the mutations.
   - **Outcome**:
     - Identify surviving mutations and improve test cases to kill them.

2. **Code Coverage Analysis with `coverage.py`**
   - **Objective**: Measure the percentage of code executed during testing.
   - **Steps**:
     - Run `coverage run -m unittest discover -s test` to execute tests with coverage tracking.
     - Generate an HTML report using `coverage html`.
   - **Outcome**:
     - Analyze uncovered lines of code and improve test cases to achieve higher coverage.

---

## Conclusion

This repository demonstrates a comprehensive approach to software testing and quality assurance, covering a wide range of testing techniques, tools, and methodologies. Each lab builds on the previous one, providing a solid foundation in testing principles and practices.

Feel free to explore the code and reports for each lab to gain deeper insights into the testing strategies employed.
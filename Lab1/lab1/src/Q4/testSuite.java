package Q4;

import org.junit.runner.RunWith;
import org.junit.runners.Suite;
import Q2.TriangleTest;
import Q3.*;

// Use the Suite runner to run the test suite
@RunWith(Suite.class)
// Specify the classes to be included in the test suite
@Suite.SuiteClasses({
        TriangleTest.class, // Include TriangleTest class in the test suite
        RETest3.class // Include RETest3 class in the test suite
})
public class testSuite {
    // This class remains empty, it is used only as a holder for the above
    // annotations
}

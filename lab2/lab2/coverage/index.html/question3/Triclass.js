var clover = new Object();

// JSON: {classes : [{name, id, sl, el,  methods : [{sl, el}, ...]}, ...]}
clover.pageData = {"classes":[{"el":22,"id":135,"methods":[{"el":21,"sc":5,"sl":4}],"name":"Triclass","sl":3}]}

// JSON: {test_ID : {"methods": [ID1, ID2, ID3...], "name" : "testXXX() void"}, ...};
clover.testTargets = {"test_28":{"methods":[{"sl":4}],"name":"testInvalidTriangle","pass":true,"statements":[{"sl":6},{"sl":7},{"sl":9},{"sl":10}]},"test_33":{"methods":[{"sl":4}],"name":"testEquilateral","pass":true,"statements":[{"sl":6},{"sl":9},{"sl":14},{"sl":15}]},"test_41":{"methods":[{"sl":4}],"name":"testScalene","pass":true,"statements":[{"sl":6},{"sl":9},{"sl":14},{"sl":16},{"sl":19}]},"test_9":{"methods":[{"sl":4}],"name":"testIsosceles","pass":true,"statements":[{"sl":6},{"sl":9},{"sl":14},{"sl":16},{"sl":17}]}}

// JSON: { lines : [{tests : [testid1, testid2, testid3, ...]}, ...]};
clover.srcFileLines = [[], [], [], [], [28, 41, 9, 33], [], [28, 41, 9, 33], [28], [], [28, 41, 9, 33], [28], [], [], [], [41, 9, 33], [33], [41, 9], [9], [], [41], [], [], []]

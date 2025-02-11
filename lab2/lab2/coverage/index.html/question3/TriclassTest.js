var clover = new Object();

// JSON: {classes : [{name, id, sl, el,  methods : [{sl, el}, ...]}, ...]}
clover.pageData = {"classes":[{"el":48,"id":114,"methods":[{"el":19,"sc":5,"sl":16},{"el":23,"sc":5,"sl":21},{"el":28,"sc":5,"sl":25},{"el":34,"sc":5,"sl":30},{"el":39,"sc":5,"sl":36},{"el":47,"sc":5,"sl":41}],"name":"TriclassTest","sl":5}]}

// JSON: {test_ID : {"methods": [ID1, ID2, ID3...], "name" : "testXXX() void"}, ...};
clover.testTargets = {"test_28":{"methods":[{"sl":41}],"name":"testInvalidTriangle","pass":true,"statements":[{"sl":42},{"sl":43},{"sl":44},{"sl":45},{"sl":46}]},"test_33":{"methods":[{"sl":25}],"name":"testEquilateral","pass":true,"statements":[{"sl":26},{"sl":27}]},"test_41":{"methods":[{"sl":36}],"name":"testScalene","pass":true,"statements":[{"sl":37},{"sl":38}]},"test_9":{"methods":[{"sl":30}],"name":"testIsosceles","pass":true,"statements":[{"sl":31},{"sl":32},{"sl":33}]}}

// JSON: { lines : [{tests : [testid1, testid2, testid3, ...]}, ...]};
clover.srcFileLines = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [33], [33], [33], [], [], [9], [9], [9], [9], [], [], [41], [41], [41], [], [], [28], [28], [28], [28], [28], [28], [], []]

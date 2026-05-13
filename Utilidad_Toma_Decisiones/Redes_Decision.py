class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, *, value=None, impurity=0.0, is_leaf=False, n_samples=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value
        self.impurity = impurity
        self.is_leaf = is_leaf
        self.n_samples = n_samples
        def __init__(self, max_depth=None, min_samples_split=2, min_samples_leaf=1, 
        min_impurity_decrease=0.0, task='classification', impurity='gini', alpha=0.0):

    self.max_depth = max_depth
    self.min_samples_split = min_samples_split
    self.min_samples_leaf = min_samples_leaf
    self.min_impurity_decrease = min_impurity_decrease
    self.task = task
    self.impurity = impurity
    self.root = None
    self.alpha = alpha
    def _calculate_gini(self, y):
    _, counts = np.unique(y, return_counts=True)
    probabilities = counts / counts.sum()
    return 1 - np.sum(probabilities**2)

def _calculate_entropy(self, y):
    _, counts = np.unique(y, return_counts=True)
    probabilities = np.clip(counts / counts.sum(), 1e-10, 1)
    return -np.sum(probabilities * np.log2(probabilities))

def _calculate_mse(self, y):
    return np.mean((y - np.mean(y)) ** 2)

def _calculate_impurity(self, y):
    if self.task == 'classification':
        if self.impurity == 'gini':
            return self._calculate_gini(y)
        elif self.impurity == 'entropy':
            return self._calculate_entropy(y)
        else:
            raise ValueError(f"Unknown impurity criterion: {self.impurity}")
    elif self.task == 'regression':
        if self.impurity == 'mse':
            return self._calculate_mse(y)
        else:
            raise ValueError(f"Unknown task: {self.task}")
            def _best_split(self, X, y):
    n_samples = len(y)
    best_feature, best_threshold, best_gain = None, None, float('-inf')
    current_impurity = self._calculate_impurity(y)
    for feature_idx in range(self.n_features):
        thresholds = np.unique(X[:, feature_idx])
        for threshold in thresholds:
            X_left, y_left, X_right, y_right = self._split_data(X, y, feature_idx, threshold)
            if len(y_left) < self.min_samples_leaf or len(y_right) < self.min_samples_leaf:
                continue
            left_impurity = self._calculate_impurity(y_left)
            right_impurity = self._calculate_impurity(y_right)
            weighted_impurity = (len(y_left) * left_impurity + len(y_right) * right_impurity) / n_samples
            impurity_gain = current_impurity - weighted_impurity
            if impurity_gain > best_gain and impurity_gain >= self.min_impurity_decrease:
                best_feature = feature_idx
                best_threshold = threshold
                best_gain = impurity_gain
    return best_feature, best_threshold
    def _build_tree(self, X, y, depth=0):
    n_samples = len(y)
    node_impurity = self._calculate_impurity(y)
    node_value = self._calculate_leaf_value(y)
    node = Node(value=node_value, impurity=node_impurity, is_leaf=True, n_samples=n_samples)

    if (self.max_depth is None or depth < self.max_depth) and len(y) >= self.min_samples_split and len(np.unique(y)) > 1:
        best_feature, best_threshold = self._best_split(X, y)
        if best_feature is not None:
            X_left, y_left, X_right, y_right = self._split_data(X, y, best_feature, best_threshold)
            left_node = self._build_tree(X_left, y_left, depth + 1)
            right_node = self._build_tree(X_right, y_right, depth + 1)

            node.feature = best_feature
            node.threshold = best_threshold
            node.left = left_node
            node.right = right_node
            node.is_leaf = False

    return node
    def _predict_one(self, x):
    node = self.root
    while node is not None and not node.is_leaf:
        if x[node.feature] <= node.threshold:
            node = node.left
        else:
            node = node.right
    return node.value if node is not None else None

def predict(self, X):
    X = np.array(X)
    return np.array([self._predict_one(sample) for sample in X])
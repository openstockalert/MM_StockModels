**Mode Evaluation**
--------------
Accuracy is the proportion of correct predictions out of the total number of predictions. It is calculated as the ratio of correctly classified instances to the total number of instances.
Precision is the ratio of true positives (correctly predicted positive instances) to the sum of true positives and false positives (incorrectly predicted positive instances).
Recall is the ratio of true positives to the sum of true positives and false negatives (incorrectly predicted negative instances).
F1 Score is the harmonic mean of precision and recall. It provides a balanced measure of the model's performance, taking into account both precision and recall.
ROC AUC (Receiver Operating Characteristic Area Under the Curve) is a metric used to evaluate the performance of binary classification models. It measures the ability of the model to distinguish between positive and negative classes. A higher ROC AUC score indicates better performance.


    explain this result:
    Logistic Regression Accuracy: 55.68%
                precision    recall  f1-score   support

            0       0.48      0.37      0.42        38
            1       0.59      0.70      0.64        50

        accuracy                           0.56        88
    macro avg       0.54      0.53      0.53        88
    weighted avg       0.55      0.56      0.55        88


        This result is a classification report for a logistic regression model. Here's a breakdown of what each part means:

        **Accuracy:** 55.68%

        * This is the overall accuracy of the model, which means that the model correctly predicted 55.68% of the samples.

        **Classification Report:**

        * **Class 0:** This refers to the first class in the classification problem (e.g. "not buying" or "not responding").
            + **Precision:** 0.48
                - This means that out of all the samples that the model predicted as class 0, 48% of them were actually class 0.
            + **Recall:** 0.37
                - This means that out of all the actual class 0 samples, the model correctly predicted 37% of them as class 0.
            + **F1-score:** 0.42
                - This is the harmonic mean of precision and recall, and it gives a sense of the model's performance on class 0.
            + **Support:** 38
                - This is the number of actual class 0 samples in the test set.
        * **Class 1:** This refers to the second class in the classification problem (e.g. "buying" or "responding").
            + **Precision:** 0.59
                - This means that out of all the samples that the model predicted as class 1, 59% of them were actually class 1.
            + **Recall:** 0.70
                - This means that out of all the actual class 1 samples, the model correctly predicted 70% of them as class 1.
            + **F1-score:** 0.64
                - This is the harmonic mean of precision and recall, and it gives a sense of the model's performance on class 1.
            + **Support:** 50
                - This is the number of actual class 1 samples in the test set.

        **Macro Average:**

        * **Precision:** 0.54
            + This is the average precision across both classes.
        * **Recall:** 0.53
            + This is the average recall across both classes.
        * **F1-score:** 0.53
            + This is the average F1-score across both classes.
        * **Support:** 88
            + This is the total number of samples in the test set.

        **Weighted Average:**

        * **Precision:** 0.55
            + This is the weighted average precision across both classes, where the weights are the support values.
        * **Recall:** 0.56
            + This is the weighted average recall across both classes, where the weights are the support values.
        * **F1-score:** 0.55
            + This is the weighted average F1-score across both classes, where the weights are the support values.
        * **Support:** 88
            + This is the total number of samples in the test set.

        Overall, this report suggests that the model is performing slightly better on class 1 than on class 0, and that it has a moderate level of accuracy.

**Do we get same model if trained with same data**


    No, even if you use the same set of data to train a model, you may not get the same model. Here are some reasons why:

    1. **Random initialization**: Many machine learning algorithms, including logistic regression, neural networks, and decision trees, use random initialization of weights or parameters. This means that even if you use the same data, the model may start with different weights and converge to a different solution.
    2. **Stochastic optimization**: Many optimization algorithms used in machine learning, such as stochastic gradient descent (SGD), are stochastic in nature. This means that the optimization process involves randomness, and the model may converge to a different solution even if the data is the same.
    3. **Non-convex optimization**: Many machine learning models, including neural networks, have non-convex optimization problems. This means that the optimization process may converge to a local minimum, and different initializations or random seeds may lead to different local minima.
    4. **Regularization**: Regularization techniques, such as L1 or L2 regularization, can also affect the model's convergence. Different regularization strengths or types may lead to different models even if the data is the same.
    5. **Implementation details**: Different implementations of the same algorithm may have different behaviors, such as different default parameters or optimization methods. This can lead to different models even if the data is the same.

    However, if you use the same data, algorithm, and hyperparameters, and you fix the random seed, you should get the same model. This is because the random seed controls the randomness in the optimization process, and fixing it ensures that the model converges to the same solution.

    To get the same model, you can try the following:

    * Use the same data and algorithm.
    * Fix the random seed using a library-specific function, such as `np.random.seed()` in NumPy or `torch.manual_seed()` in PyTorch.
    * Use the same hyperparameters and optimization method.
    * Verify that the implementation details are the same.

    By following these steps, you should be able to get the same model even if you train it multiple times.


**A Promising Model**
            Total Sample Count: 2443
            Model Selected Count: 132
            Model Selected/Total Count Percentage: 5.40%

            Sum of S&P_1day_up: 91
            Percentage of S&P_1day_up: 68.94%
            Mean of SP500_Change_1day: 13.96
            Std Dev of SP500_Change_1day: 40.94

            Sum of S&P_3day_up: 83
            Percentage of S&P_3day_up: 62.88%
            Mean of SP500_Change_3day: 17.01
            Std Dev of SP500_Change_3day: 80.89

            Sum of S&P_5day_up: 87
            Percentage of S&P_5day_up: 65.91%
            Mean of SP500_Change_5day: 23.9
            Std Dev of SP500_Change_5day: 90.27

            Sum of S&P_14day_up: 99
            Percentage of S&P_14day_up: 75.00%
            Mean of SP500_Change_14day: 54.96
            Std Dev of SP500_Change_14day: 135.66
            
            Sum of S&P_28day_up: 104
            Percentage of S&P_28day_up: 78.79%
            Mean of SP500_Change_28day: 88.77
            Std Dev of SP500_Change_28day: 181.25

![Model](ModelvsControl.png)
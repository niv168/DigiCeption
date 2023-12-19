import streamlit as st
def app():
    st.title("ABOUT THIS PROJECT")
    st.write('##')
    st.write("""
             Choosing the right algorithms for phishing URL detection is crucial for effective cybersecurity. Phishing attacks constantly evolve, so it's essential to use a combination of techniques to stay ahead.
               Here's a guide on how to choose algorithms for phishing URL detection
             """)
    st.subheader("Here is the list of all algorithms that we have used in this project")
    st.write('##')
    st.subheader(" NAIVE BAYES"
       
    )
    st.write('##')
    st.write(
        """ 
     Naive Bayes is a classification algorithm commonly used in the field of machine learning, including in various forms of detection tasks such as spam email detection, sentiment analysis, and yes, even in phishing detection. The term "naive" refers to the simplifying assumption the algorithm makes about the independence of features, which is often unrealistic but still surprisingly effective in practice.
"""
    )
    st.write("""
             - In the context of detection, the algorithm is trained on a labeled dataset containing examples of both the positive class (e.g., phishing URLs) and the negative class (e.g., legitimate URLs).
             - It calculates the probabilities of observing each feature given the class label (e.g., P(feature|phishing) and P(feature|legitimate)).
             - It also calculates the prior probabilities of the classes (P(phishing) and P(legitimate)).""")
    st.write('##')
    st.subheader(" SUPPORT VECTOR MACHINE"
       
    )
    st.write('##')
    st.write("""
           Support Vector Machine (SVM) is a powerful machine learning algorithm used in various detection tasks, including but not limited to intrusion detection, spam email detection, and malware detection. SVM is particularly effective in binary classification problems where the goal is to separate data into two distinct classes. Here's an overview of how SVM is used in detection:
             """)
    st.write("""
            - SVM is primarily designed for binary classification, meaning it's used to separate data into two classes: positive (e.g., malicious or spam) and negative (e.g., benign or legitimate).
            - SVM's main objective is to find a hyperplane that maximizes the margin between the two classes. The margin is the distance between the hyperplane and the nearest data points from each class. This margin maximization approach helps SVM generalize well to unseen data.
            - The data points closest to the hyperplane, called support vectors, play a crucial role in defining the hyperplane. These vectors are the most challenging instances to classify correctly and heavily influence the position of the hyperplane.
              
             """)
    st.write('##')
    st.subheader(" DECISION TREE"
       
    )
    st.write('##')
    st.write("""
           Decision trees are a popular and interpretable machine learning algorithm used in various detection tasks, including intrusion detection, fraud detection, and anomaly detection. They are particularly useful for tasks that involve classification or regression by creating a hierarchical tree-like structure of decisions. 
             Here's an overview of how decision trees are used in detection:
             """)
    st.write("""
          - Decision trees are designed to make decisions in a hierarchical and step-by-step manner. Each node in the tree represents a decision or a test on a specific feature or attribute.
          - At each node, the decision tree algorithm selects the most informative feature to split the data. The goal is to choose the feature that best separates the data into different classes or groups. 
          - The decision tree algorithm uses various criteria to determine the best feature and threshold for splitting, such as Gini impurity, entropy, or information gain.    
             """)
    
    st.write('##')
    st.subheader(" K Neighbours"
       
    )
    st.write('##')
    st.write("""
           The k-Nearest Neighbors (k-NN) algorithm is a simple yet effective machine learning technique used in various detection tasks, including intrusion detection, anomaly detection, and spam detection. It's a non-parametric and instance-based algorithm that relies on the similarity between data points to make predictions or decisions. Here's an overview of how k-NN is used in detection:
             """)
    st.write("""
          - The core idea behind k-NN is the nearest neighbor principle, which states that objects in a dataset are more similar to their nearest neighbors than to objects farther away. In the context of detection, similarity is often measured as distance.
          - When making predictions or decisions, k-NN calculates the distance between the data point to be classified and all other data points in the training dataset.
          - For classification tasks, k-NN employs a majority voting mechanism among the k-nearest neighbors. It assigns the class label that is most frequent among these neighbors to the data point being classified.
             """
    )

    st.write('##')
    st.subheader("Random Forest"
       
    )
    st.write('##')
    st.write("""
            Random Forest is a versatile and powerful ensemble learning algorithm frequently used in detection tasks, including intrusion detection, fraud detection, spam email detection, and malware detection. It combines the strength of multiple decision trees to improve overall accuracy and reduce the risk of overfitting. 
             Here's an overview of how Random Forest is used in detection:
             """)
    st.write("""
          - At the core of Random Forest are decision trees, which are simple models used for classification and regression tasks.
          - Each decision tree learns to make decisions by recursively splitting the data based on features to create a tree-like structure with leaves representing class labels.
          - In classification tasks, each decision tree in the Random Forest independently predicts the class label for a given input. The final prediction is determined through a voting mechanism, where the class that receives the most votes from the trees becomes the overall prediction.      
             """
    )


    
   

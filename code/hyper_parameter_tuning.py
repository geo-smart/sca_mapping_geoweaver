# prepare data 
data = pd.read_csv('./data/samples/sample_10K.csv', index_col = False)
print("Sample dimentions:".format(), data.shape)
data.head()
X = data[['blue','green','red','nir']]
y = data['label']

# customize models with different sample sizes
models = get_models_size()
results, names = list(), list()
for name, model in models.items():
    # evaluate models using k-fold cross-validation
    scores = evaluate_model(model, X, y)
    results.append(scores)
    names.append(name)
    # print the mean and standard deviation of models 
    print('>%s   Mean Score: %.6f (Score SD: %.6f)' % ('Sample size: ' + str(int(float(name) * 10000)), scores.mean(), scores.std()))
    
# display model performance 
plt.figure(figsize=(10,5))
plt.boxplot(results, labels=names, showmeans=True)
plt.show()

# customize models with different model feature sizes
models = get_models_feature()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    # evaluate models using k-fold cross-validation
    scores = evaluate_model(model, X, y)
    results.append(scores)
    names.append(name)
    # print the mean and standard deviation of models 
    # print('>%s %.3f (%.3f)' % (name, scores.mean(), scores.std()))
    print('>%s   Mean Score: %.6f (Score SD: %.6f)' % ('Features: ' + name, scores.mean(), scores.std()))
# display model performance 
plt.boxplot(results, labels=names, showmeans=True)
plt.show()

# customize models with different tree numbers
models = get_models_tree()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    # evaluate models using k-fold cross-validation
    scores = evaluate_model(model, X, y)
    results.append(scores)
    names.append(name)
    # print the mean and standard deviation of models 
    # print('>%s %.3f (%.3f)' % (name, scores.mean(), scores.std()))
    print('>%s   Mean Score: %.6f (Score SD: %.6f)' % ('Tree numbers: ' + name, scores.mean(), scores.std()))
# display model performance 
plt.boxplot(results, labels=names, showmeans=True)
plt.show()

# customize models with different tree depths
models = get_models_depth()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
     # evaluate models using k-fold cross-validation
    scores = evaluate_model(model, X, y)
    results.append(scores)
    names.append(name)
    # print the mean and standard deviation of models 
    # print('>%s %.3f (%.3f)' % (name, scores.mean(), scores.std()))
    print('>%s   Mean Score: %.6f (Score SD: %.6f)' % ('Tree Depth: ' + name, scores.mean(), scores.std()))
# display model performance 
plt.figure(figsize=(10,5))
plt.boxplot(results, labels=names, showmeans=True)
plt.show()

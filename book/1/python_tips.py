# Python有pickle这个便利的功能。这个功能可以将程序运行中的对
# 象保存为文件。如果加载保存过的pickle文件，可以立刻复原之前
# 程序运行中的对象。用于读入MNIST数据集的 load_mnist() 函数内
# 部也使用了pickle功能（在第2次及以后读入时）。利用pickle功能，
# 可以高效地完成MNIST数据的准备工作


#观察本书源代码可知，上述代码在 mnist_show.py 文件中。 mnist_show.py 文件的当前目录是 ch03 ，
# 但包含 load_mnist() 函数的 mnist.py 文件在 dataset 目录下。因此， mnist_show.py 文件不能跨目
# 录直接导入 mnist.py 文件。 sys.path.append(os.pardir) 语句实际上是把父目录 deep-learning-
# from-scratch 加入到 sys.path （Python的搜索模块的路径集）中，从而可以导入 deep-learning-
# from-scratch 下的任何目录（包括 dataset 目录）中的任何文件。——译者注
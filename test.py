import tensorflow as tf

graph = tf.Graph()      #to​ get the default graph.
with graph.as_default():
	x = tf.constant(5, name = "x_value")
	y = tf.constant(3, name= "y_value")
	sum = tf.add(x, y, name="added_value")
	with tf.session() as session :
		print("Result : ", sum.eval() )
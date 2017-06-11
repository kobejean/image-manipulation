import tensorflow as tf
import numpy as np
import time

# adapted from https://gist.github.com/dave-andersen/265e68a5e879b5540ebc

MAX_ITERS = 1000

def kmeans(list_pix, k):
    start = time.time()

    n = len(list_pix)
    # print(n)
    np_pix = np.array(list_pix)
    # print(np_pix)
    i_pix = tf.placeholder(tf.uint8, shape=(n, 3), name="int_pix_vals")
    f_pix = tf.Variable(tf.to_float(i_pix)/255, name="float_pix_vals")

    cluster_assignments = tf.Variable(tf.zeros([n], dtype=tf.int64))
    centroids = tf.Variable(tf.slice(tf.random_shuffle(f_pix.initialized_value()), [0,0], [k,-1]), name="centroids")

    # Replicate to N copies of each centroid and K copies of each
    # point, then subtract and compute the sum of squared distances.
    rep_centroids = tf.reshape(tf.tile(centroids, [n, 1]), [n, k, 3])
    rep_f_pix = tf.reshape(tf.tile(f_pix, [1, k]), [n, k, 3])
    sum_squares = tf.reduce_sum(tf.square(rep_f_pix - rep_centroids), axis=2)

    # Use argmin to select the lowest-distance point
    best_centroids = tf.argmin(sum_squares, 1)
    did_assignments_change = tf.reduce_any(tf.not_equal(best_centroids, cluster_assignments))

    def bucket_mean(data, bucket_ids, num_buckets):
        total = tf.unsorted_segment_sum(data, bucket_ids, num_buckets)
        count = tf.unsorted_segment_sum(tf.ones_like(data), bucket_ids, num_buckets)
        return total / count

    means = bucket_mean(f_pix, best_centroids, k)

    # Do not write to the assigned clusters variable until after
    # computing whether the assignments have changed - hence with_dependencies
    with tf.control_dependencies([did_assignments_change]):
        do_updates = tf.group(
            centroids.assign(means),
            cluster_assignments.assign(best_centroids))

    init = tf.global_variables_initializer()

    with tf.Session() as session:
        session.run(init, feed_dict={i_pix: np_pix})
        changed = True
        iters = 0

        while changed and iters < MAX_ITERS:
            iters += 1
            [changed, _] = session.run([did_assignments_change, do_updates])

        [centers, assignments] = session.run([centroids, cluster_assignments])
        end = time.time()
        print(("Found in %.2f seconds" % (end-start)), iters, "iterations")
        print("Centroids:")
        print(centers)
        print("Cluster assignments:", assignments)

        print("Final rgbs:")
        i_centroids = tf.cast(tf.round(centers * 255), tf.uint8)
        fin_pix_gather = tf.gather(i_centroids, assignments)


        fin_pix = session.run(fin_pix_gather)
        return list(map(tuple, fin_pix))
    return []

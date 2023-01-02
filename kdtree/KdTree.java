/* *****************************************************************************
 *  Name:
 *  Date:
 *  Description:
 **************************************************************************** */

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;

public class KdTree {
    private Node root;
    private int size;

    private PointComparator comp;

    /**
     * construct an empty set of points
     */
    public KdTree() {
        root = null;
        size = 0;
        comp = new PointComparator();

    }

    public static void main(String[] args) {

        In reader;
        KdTree t = new KdTree();

        reader = new In("input5.txt");

        while (!reader.isEmpty()) {
            String[] line = reader.readLine().split(" ");
            Point2D p = new Point2D(Double.parseDouble(line[0]), Double.parseDouble(line[1]));
            t.insert(p);
            System.out.println(Arrays.toString(line));

            // read next line
        }
        System.out.println(t);

        reader.close();

    }

    /**
     * @return is the set empty?
     */
    public boolean isEmpty() {
        return this.size == 0;
    }

    /**
     * @return number of points in the set
     */
    public int size() {
        return this.size;
    }

    /**
     * @param p add the point to the set (if it is not already in the set)
     */
    public void insert(Point2D p) {
        if (root == null) {
            root = new Node(p);
            size++;
        }
        else {
            this.insert(p, root, 0);
        }

    }

    private void insert(Point2D p, Node x, int level) {
        int compare = comp.compare(p, x.getPoint(), level);

        if (compare < 0) {
            if (x.hasLeft()) {
                this.insert(p, x.getLeft(), level + 1);
            }
            else {
                x.left = new Node(p);
                size++;
            }
        }
        else if (compare > 0) {
            if (x.hasRight()) {
                this.insert(p, x.getRight(), level + 1);
            }
            else {
                x.right = new Node(p);
                size++;
            }
        }
        else {
            return;
        }
    }

    /**
     * @param p
     * @return does the set contain point p?
     */
    public boolean contains(Point2D p) {
        return this.contains(p, root, 0);
    }

    private boolean contains(Point2D p, Node x, int level) {
        int compare = comp.compare(p, x.getPoint(), level);

        if (compare < 0) {
            if (x.hasLeft()) {
                return this.contains(p, x.getLeft(), level + 1);
            }
            return false;
        }
        else if (compare > 0) {
            if (x.hasRight()) {
                return this.contains(p, x.getRight(), level + 1);
            }
            return false;
        }
        else {
            return true;
        }
    }

    /**
     * draw all points to standard draw
     */
    public void draw() {
        PointIterator iter = new PointIterator(root);

        for (PointIterator it = iter; it.hasNext(); ) {
            Point2D p = it.next();
            p.draw();
        }

    }

    /**
     * all points that are inside the rectangle (or on the boundary)
     *
     * @param rect
     * @return
     */
    public Iterable<Point2D> range(RectHV rect) {
        return null;
    }

    /**
     * a nearest neighbor in the set to point p; null if the set is empty
     *
     * @param p
     * @return
     */
    public Point2D nearest(Point2D p) {
        return null;

    }

    public String toString() {
        ArrayList<ArrayList<Node>> levels = new ArrayList<>();
        if (root != null) {
            ArrayList<Node> first = new ArrayList<>();
            first.add(root);
            levels.add(first);
        }

        while (!levels.get(levels.size() - 1).isEmpty()) {
            levels.add(new ArrayList<>());

            for (Node n : levels.get(levels.size() - 2)) {
                if (n.hasLeft()) {
                    levels.get(levels.size() - 1).add(n.getLeft());
                }
                if (n.hasRight()) {
                    levels.get(levels.size() - 1).add(n.getRight());
                }
            }
        }
        return levels.toString();
    }

    private static class PointIterator implements Iterator<Point2D> {
        private ArrayList<Point2D> pointList;
        private int i = 0;

        public PointIterator(Node root) {
            pointList = new ArrayList<>();
            LinkedList<Node> queue = new LinkedList<>();
            if (root != null) {
                queue.add(root);
                queue.add(root);
            }

            while (!queue.isEmpty()) {
                Node x = queue.removeFirst();
                pointList.add(x.getPoint());


                if (x.hasLeft()) {
                    queue.add(x.getLeft());
                }
                if (x.hasRight()) {
                    queue.add(x.getRight());
                }

            }
        }

        /**
         * Returns {@code true} if the iteration has more elements.
         * (In other words, returns {@code true} if {@link #next} would
         * return an element rather than throwing an exception.)
         *
         * @return {@code true} if the iteration has more elements
         */
        public boolean hasNext() {
            return this.i < pointList.size();
        }

        /**
         * Returns the next element in the iteration.
         *
         * @return the next element in the iteration
         * @throws NoSuchElementException if the iteration has no more elements
         */
        public Point2D next() {
            return pointList.get(i++);
        }
    }


    private class PointComparator {
        /**
         * @param a     point 1
         * @param b     point 2
         * @param level tree level starting from 0
         * @return -1 if a < b, 1 if a > b else 0
         */
        public int compare(Point2D a, Point2D b, int level) {
            if (level % 2 == 0) {
                double ax = a.x();
                double bx = b.x();
                if (ax < bx) {
                    return -1;
                }
                else if (ax > bx) {
                    return 1;
                }
                else {
                    if (a.y() == b.y()) {
                        return 0;
                    }
                    return -1;
                }

            }
            else {
                double ay = a.y();
                double by = b.y();
                if (ay < by) {
                    return -1;
                }
                else if (ay > by) {
                    return 1;
                }
                else {
                    if (a.x() == b.x()) {
                        return 0;
                    }
                    return -1;
                }
            }
        }
    }

    private static class Node {
        private Point2D p;
        private Node left;
        private Node right;

        public Node(Point2D point) {
            this.p = point;
            left = null;
            right = null;
        }

        public Point2D getPoint() {
            return this.p;
        }

        public Node getLeft() {
            return left;
        }

        public Node getRight() {
            return right;
        }

        public void setLeft(Node left) {
            this.left = left;
        }

        public void setRight(Node right) {
            this.right = right;
        }

        public boolean hasLeft() {
            return this.left != null;
        }

        public boolean hasRight() {
            return this.right != null;
        }

        public String toString() {
            return p.toString();
        }
    }
}

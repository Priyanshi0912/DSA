class Solution {
    long gcd(long a, long b){
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    long InternalCount(long[] p, long[] q, long[] r) {
        //I = A - (B / 2) + 1
        
        long x1 = p[0];
        long y1 = p[1];
        long x2 = q[0];
        long y2 = q[1];
        long x3 = r[0];
        long y3 = r[1];

        long area = Math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2));
        area /= 2;  // Integer division to avoid floating-point issues

        long first = gcd(Math.abs(x1 - x2), Math.abs(y1 - y2));
        long second = gcd(Math.abs(x2 - x3), Math.abs(y2 - y3));
        long third = gcd(Math.abs(x3 - x1), Math.abs(y3 - y1));
        long b = first + second + third;

        return area - (b / 2) + 1;
    }
}

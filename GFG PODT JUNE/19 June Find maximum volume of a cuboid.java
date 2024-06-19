class Solution {

    double maxVolume(double perimeter, double area) {
        double length = (double)(perimeter - Math.sqrt(perimeter*perimeter - 24*area))/12;
        double height = (perimeter/4) - (2*(length));
        double vol = length*length*height;
        return vol;
        // code here
    }
}

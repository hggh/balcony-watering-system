$fn=190;


module inlay() {
    difference() {
        cube([60, 20, 8]);
        translate([1.6, 4, 2]) {
            cube([5, 12, 10]);
        }
        translate([30, 5, -1]) {
            cube([15, 10, 20]);
        }
    }
}

module holder() {
    
    cube([35, 20, 1.2]);
    translate([5, 5.5, 0]) {
        cube([15-1, 10-1, 45]);
    }
}

module lid() {
    cube([20, 20, 1.2]);
}

translate([54.5, 0, 20]) {
    inlay();
}

translate([80, 0, 0]) {
    holder();
}

translate([80, 5, 50]) {
    lid();
}
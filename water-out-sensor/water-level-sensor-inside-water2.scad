$fn=190;

include <BOSL/constants.scad>
use <BOSL/shapes.scad>


translate([-5, 3, -4]) {
    cube([12, 14, 14]);
    cube([8, 14, 19]);
    cube([40, 14, 1.6]);
}
rotate([90, 0, 0]) {
    translate([3, 10/2, -19.5])
        cylinder(d=3, h=19);
}

translate([20, 10, -4]) {
    cylinder(d=3, h=3);
}

translate([30, 10, -4]) {
    cylinder(d=3, h=3);
}


difference() {
    union() {
        translate([5, 0,0]) {
            cube([55, 20, 10]);
        }
        translate([5, 20, 5]) {
            rotate([90, 0, 0]) cylinder(d=10, h=20);
        }
    }
    // place for magnets
    translate([60-5-1.2, (20-12)/2, 1.2]) {
        cube([5, 12, 16]);
    }
    // holder pins cutout
    rotate([90, 0, 0]) {
        translate([3, 10/2, -21])
        cylinder(d=4, h=60);
    }
    
    translate([0, 2, 0]) {
        cube([10, 16, 20]);
    }    
}
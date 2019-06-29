/**
 *
 */

#include <opencv/opencv.hpp>
#include <iostream>


int main(int argc, char* argv)
{
    // TODO: Instantiate LaneFinder object
    VideoCapture cap("/home/russell/Autonomous-Driving-Stack/development/perception/lane_following/test_videos/lane_test_1.mp4");
    std::cout << "Success" << endl;
    return 0;
}
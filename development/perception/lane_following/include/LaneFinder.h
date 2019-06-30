/**
 * @file LaneFinder.h
 * @author George Murray 
 * @brief 
 * @version 0.1
 * @date 2019-06-29
 * 
 * 
 * 
 */
#ifndef AUTONOMOUS_DRIVING_STACK_LANEFINDER_H
#define AUTONOMOUS_DRIVING_STACK_LANEFINDER_H

#include <opencv2/opencv.hpp>

using namespace cv;

/**
 * @brief A class that when instantiated creates an opencv2 stream and detects lane lines
 * within each frame and computes the steering command based on the curvature of the lane
 * 
 */
class LaneFinder {

private:
	VideoCapture cap_;
    string file_path_;
    string window_name_;
    void detectCanny();
    void gaussianBlur();
    void applySobel();
    void applyBirdseye();
    void createWindow();
public:
    LaneFinder(string video_path);
    double steering_command_;
    void init();

};

#endif //AUTONOMOUS_DRIVING_STACK_LANEFINDER_H

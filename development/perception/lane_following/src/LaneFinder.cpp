/**
 * @file LaneFinder.cpp
 * @author George Murray 
 * @brief 
 * @version 0.1
 * @date 2019-06-29
 * 
 * 
 */

// Standard imports
#include <iostream>
// LaneFinder imports
#include "LaneFinder.h"
// OpenCV imports
#include <opencv2/opencv.hpp>

using namespace cv;
/**
 * @brief Construct a new Lane Finder:: Lane Finder object
 * 
 * @param video_path: The path of the video file we are going to detect lane lines on
 */
LaneFinder::LaneFinder(string video_path) :file_path_(video_path), cap_(video_path) 
{
    window_name_ = "Lane Detection";
}

// Create cv2 window to output video with lanes detected
void LaneFinder::createWindow()
{
    namedWindow(window_name_, WINDOW_AUTOSIZE);
}
// Initialize lane detection
void LaneFinder::init()
{
    // TODO: Start cv2 video stream
    // cap_(file_path_);
    if (cap_.isOpened() == false)
    {
        std::cout << "Cannot open the video file" << std::endl;
        return;
    }
    createWindow();
    // Keep streaming video 
    while (true)
    {
        // Declare frame to read from the video stream
        Mat frame;
        bool end_of_video = cap_.read(frame);
        // Check if we are at the end of the stream
        if (end_of_video == false)
        {
            std::cout << "Found the end of the video" << std::endl;
            break;
        }
        // TODO: Perform CV algorithms for lane detection

        // Output frame to window
        imshow(window_name_, frame);
        // Exit if user presses esc key
        if (waitKey(10) == 27)
        {
            std::cout << "Esc key pressed. Stopping video" << std::endl;
        }
    }

}

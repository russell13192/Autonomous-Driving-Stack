/**
 * @file main.cpp
 * @author George Murray 
 * @brief 
 * @version 0.1
 * @date 2019-06-29
 * 
 * @copyright Copyright (c) 2019
 * 
 */

#include <opencv2/opencv.hpp>
#include <iostream>
#include "LaneFinder.h"



/**
 * @brief 
 * 
 * @param argc 
 * @param argv 
 * @return int 
 */
int main(int argc, char* argv)
{
    // TODO: Instantiate LaneFinder object
    string video_path = "../test_videos/lane_test_1.mp4";
    LaneFinder(video_path);
    LaneFinder.init();
    return 0;
}
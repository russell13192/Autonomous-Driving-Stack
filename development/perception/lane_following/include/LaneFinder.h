/**
 * Author: George Murray
 */

#ifndef AUTONOMOUS_DRIVING_STACK_LANEFINDER_H
#define AUTONOMOUS_DRIVING_STACK_LANEFINDER_H

#include <opencv/opencv.hpp>
#include "opencv2/highgui.hpp"

using namespace cv;

class LaneFinder {
private:
	VideoCapture cap_;
public:
	string file_path_;
	LaneFinder(string file_path_) : file_path_(file_path_)
	{
		cap_(file_path_);
	}
};

#endif //AUTONOMOUS_DRIVING_STACK_LANEFINDER_H

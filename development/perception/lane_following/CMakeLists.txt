project(LaneFinding)

cmake_minimum_required(VERSION 3.5)
add_definitions(-std=c++11)
set(sources stc/main.cpp src/LaneFinder.cpp include/LaneFinder.h)
find_package(OpenCV REQUIRED)
target_link_libraries(
        ${PROJECT_NAME}
        ${OpenCV_LIBS}
)
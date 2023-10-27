cmake_minimum_required(VERSION 3.26)
project(All_in_One)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories("twenty four")

add_executable(All_in_One
        "twenty four/c++/main.cpp")

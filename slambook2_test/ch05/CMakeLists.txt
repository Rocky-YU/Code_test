# 声明要求的cmake最低版本
cmake_minimum_required(VERSION 2.8)

# 声明一个cmake工程
# project( useGeometry )
project( plot  )


# 添加一个可执行程序
# 语法：add_executable( 程序名  源代码文件 )
# add_executable( helloslam  helloslam.cpp)
# add_executable(useGeometry  useGeometry.cpp)

# add_library( hello_share SHARED libhelloslam.cpp)
# target_link_libraries(usehello hello_share)

#pangolin

find_package(Pangolin)
include_directories( ${Pangolin_INCLUDE_DIRS} )
add_executable(plot  plotTrajectory.cpp)
target_link_libraries(plot ${OpenCV_LIBS} ${PCL_LIBRARIES} ${Pangolin_LIBRARIES})

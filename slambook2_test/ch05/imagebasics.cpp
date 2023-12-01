# include <iostream>
# include <chrono>

using namespace std;
# include <openvn2/core/core.hpp>
# include <opencv2/highgui/highgui.cpp>

string image_file = "./distorted.png";   // 请确保路径正确

int main(int argc, char **argv){
    cv::Mat image;
    image = cv:::imread(image_file);

    if (image.data == nullptr){
        cout<< " the file of image "<< image_file << "not find "<<endl;
        return 0;
    }

    cout << "width"<< image.cols<<endl;
    cout << "high" << image.rows<<endl;

    cv::imshow("image",image);
    cv::waitKey(0);

    if (image.type()!= CV_8UC1 && image.type() != CV_8UC3){
        cout<<"image not satified"<<endl;
        return 0;
    }
    chrono::steady_clock::time_point t1 = chrono::steady_clock::now();
    for (size_t y =0; y<image.rows; y++){
        
    }


}

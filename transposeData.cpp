#include <iostream>
#include <fstream>
#include <assert.h>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <boost/algorithm/string.hpp>

#define ROWS 10561
#define COLUMNS 6483

void errorMessage() {
    std::cout << "Usage: ./transposeData inputFile outputFile" << std::endl;
    exit(EXIT_FAILURE);
}

int main(int argc, char const *argv[])
{
    std::ifstream input;
    std::ofstream output;
    std::vector<std::vector<std::string>> dataMatrix(ROWS);
    if(argc < 3)
        errorMessage();

    input.open(argv[1]);
    output.open(argv[2]);
    std::string start;
    getline(input,start);
    
    for(int i = 0; i < ROWS; i++){
        std::vector<std::string> numbers;
        std::string name;
        std::string line;
        getline(input,name,',');
        getline(input,line);
        boost::split(numbers,line,boost::is_any_of(","));
        std::transform(numbers.begin(),numbers.end(),numbers.begin(),
                [](std::string& str){ boost::trim(str); return str;});
        std::copy(numbers.begin(),numbers.end(),std::back_inserter(dataMatrix[i]));
    }

    for(int i = 0; i < COLUMNS; i++){
        for(int j = 0; j < ROWS; j++)
            output << dataMatrix[j][i]<<" ";       
        output<<std::endl;
    }
    
    
    return 0;
}




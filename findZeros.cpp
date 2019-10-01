#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <vector>

void errorMessage() {
    std::cout << "Usage: ./findZeros inputFile outputFile" << std::endl;
    exit(EXIT_FAILURE);
}

bool notZero(char c) {
    return c != ',' && c != '0' && !std::isspace(c);
}

int main(int argc, char **argv) {

    if(argc < 3)
        errorMessage();

    std::ifstream input;
    std::ofstream output;

    input.open(argv[1]);
    output.open(argv[2]);

    std::string start;
    getline(input, start);

    output << start << std::endl;
    
    while(input.good()) {
        std::string name;
        std::string line;

        getline(input, name, ',');
        getline(input, line);

        auto it = std::find_if(line.begin(), line.end(), notZero);
        if(it != line.end())
            output << name << ',' << line << std::endl;

    }

    return 0;
}








 

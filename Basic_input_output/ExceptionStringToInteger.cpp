#include <iostream>
#include <string>

int main() {

    std::string s ;
    std::cin>>s;

    try
    {
        int i = std::stoi(s);
        std::cout << i << '\n';
    }
    catch (std::invalid_argument const &e)
    {
        std::cout << "Bad String" << '\n';
    }
    catch (std::out_of_range const &e)
    {
        std::cout << "Bad String" << '\n';
    }

    return 0;
}

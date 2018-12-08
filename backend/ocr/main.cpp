#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<array>
#include<memory>
#include<stdexcept>
#include<cstdio>

std::string exec(const char* cmd) {
	std::array<char, 128> buffer;
	std::string result;
#ifdef __linux__ 
	std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
#elif _WIN32
	std::unique_ptr<FILE, decltype(&_pclose)> pipe(_popen(cmd, "r"), _pclose);
#else

#endif
	
	if (!pipe) {
		throw std::runtime_error("popen() failed!");
	}
	while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
		result += buffer.data();
	}
	return result;
}

std::string ocr(std::string filename) {
	std::string tesseract = "tesseract ";
	tesseract.append(filename).append(" temp");
	std::string out = exec(tesseract.c_str());
	std::ifstream ifs("temp.txt");
	std::string content((std::istreambuf_iterator<char>(ifs)),
		(std::istreambuf_iterator<char>()));
	//std::cout << "out " << out << std::endl;
	//std::cout << "content " << content << std::endl;
	return content;
}

std::string run(std::string filename) {
	if (filename.find_last_of('.') == std::string::npos) {
		return "error";
	}
	std::string extention = filename.substr(filename.find_last_of(".") + 1);
	std::transform(extention.begin(), extention.end(), extention.begin(), ::tolower);

	if (extention == "png" || extention == "jpg" || extention == "bmp") {
		return ocr(filename);
	}
	else if (extention == "pdf") {
		return "PDF to do";
	}
	else {
		return "error";
	}
}

int main(int argc, char *argv[]) {
	
	if (argc == 1) {
		return -1;
	}
	std::string filename = argv[1];
	std::cout <<run(filename) << std::endl;
	

	//std::cout << extention << std::endl;
	getchar();
	return 0;
}
#include<iostream>
#include<array>
#include<memory>
#include<string>

std::string exec(const char *cmd) {
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
	tesseract.append(filename).append(" stdout -l pol");
	std::string out = exec(tesseract.c_str());
	//std::cout << "out " << out << std::endl;
	return out;
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
	std::cout << run(filename) << std::endl;


	//std::cout << extention << std::endl;
	getchar();
	return 0;
}
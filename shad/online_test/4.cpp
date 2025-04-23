//=====================имхо супер правильно===================================


#include <iostream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <cmath>

int convertTime();

struct Train
{
    Train();
    void print() const;

    char label [6] = {0};
    int start_time = 0; // in seconds from start of the day
    int end_time = 0;
    int cost = 0;

    Train* cheaper = nullptr; // ptr to train cheaper than that

};



Train::Train() {
    std::cin >> this->label;
    this->start_time = convertTime();
    this->end_time = convertTime();
    std::cin >> this->cost;
}

void Train::print() const {
    std::cout << "label: " << this->label
              << "\tstart time: " << this->start_time/3600 << ':' << this->start_time%3600/60 << ':' << this->start_time%60
              << "\t_end time: " << this->end_time/3600 << ':' << this->end_time%3600/60 << ':' << this->end_time%60
              << "\tcost: " << this->cost;
    
    if (this->cheaper != nullptr) {
        std::cout << "\tmore cheaper:" << this->cheaper->label << " with cost: " << this->cheaper->cost; 
    }
    std::cout << std::endl;
}




/**
 * @brief get time string from std::in to convert it to integer
 * @return time in seconds from start of the day
 */
int convertTime() {
    int h = 0, m = 0, s = 0;

    if (scanf("%d:%d:%d", &h, &m, &s) == 3) {
        return h * 3600 + m * 60 + s;
    }

    return -1;

}

void printSchedule(std::vector<Train>& schedule) {
    for (const auto &elem : schedule) {
        elem.print();
    }
}

void setCheapest(std::vector<Train>& schedule) {
    Train* bestTrain = &schedule[0];

    for (Train &elem : schedule) {
        if (elem.cost > bestTrain->cost) {
            elem.cheaper = bestTrain;
        } else {
            bestTrain = &elem;
        }
    }
}


Train* findCheapest(std::vector<Train>& schedule, const Train& train) {
    int begin = 0;
    int end = schedule.size() - 1;
    int middle = std::ceil(end / 2);

    // если даже на самый ранний поезд он не успевает, то дальше искать смысла нет.
    if ((schedule[0].end_time + 15 * 60) > train.start_time) {
        return nullptr;
    }

    //если в мессиве один элемент
    if (begin == end) {
        return &schedule[begin];
    }

    while (begin + 1 != end) {
        if ((schedule[middle].end_time + 15 * 60) <= train.start_time) {
            begin = middle;
        } else {
            end = middle;
        }

        middle = std::ceil(float(end + begin) / 2);
    }
    return &schedule[begin];
}

void debugFindCheapest(std::vector<Train>& schedule) {
    std::cout << "==========================foo findCheapest debuging================================\n";
    
    Train trainHome;
    Train* trainOsh = findCheapest(schedule, trainHome);
    if (trainOsh == nullptr) {
        std::cout << "no possible trains" <<std::endl;
    } else {
        trainOsh->print();
    }
}



void crossCompare(std::vector<Train>& schedule, std::vector<Train>& toHome, Train* &label1, Train* &label2) {
    int min_payment = 2 * std::pow(10, 9);

    for (Train& elem : toHome) {
        Train* sutable = findCheapest(schedule, elem);
        if (sutable == nullptr) {
            continue;
        }
        if (sutable->cheaper != nullptr) {
            sutable = sutable->cheaper;
        }

        if (sutable->cost + elem.cost < min_payment) {
            min_payment = sutable->cost + elem.cost;

            label1 = sutable;
            label2 = &elem;
        } else if ((sutable->cost + elem.cost == min_payment) && (elem.end_time < label2->end_time)) {
            // если стоит одинакого, то поменяем ответ, если elem приходит раньше
            label1 = sutable;
            label2 = &elem;
        }
    }

    if (min_payment == 2 * std::pow(10, 9)) {
        label1 = label2 = nullptr;

    }
}






int main() {
    int n = 0;
    std::cin >> n;

    std::vector<Train> toOsh (n);
    

    std::sort(toOsh.begin(), toOsh.end(), [](Train& left, Train& right) {return left.end_time < right.end_time;});                            

    //printSchedule(toOsh);

    setCheapest(toOsh);

    //std::cout << "==========================after finding cheapest================================\n";

    //printSchedule(toOsh);



    int m = 0;
    std::cin >> m;

    std::vector<Train> toHome (m);

    Train* label1 = nullptr, *label2 = nullptr;

    crossCompare(toOsh, toHome, label1, label2);

    if (label1 == nullptr || label2 == nullptr) {
        std::cout << -1 << std::endl;
    } else {
        std::cout << label1->label << "\n" << label2->label << std::endl;
    }






}
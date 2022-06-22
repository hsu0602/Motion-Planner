#include <bits/stdc++.h>
using namespace std;

string INPUT_DIR = "../docs/generates/search_input.txt";
string OUTPUT_DIR = "../docs/generates/search_result.txt";

struct point{
    double x;
    double y;
};

struct config{
    double x;
    double y;
    double theta;
};

struct polygon{
    vector<point> vertices;
};

struct obstacle{
    int polynum = 0;
    vector <polygon> polys;
    config cg;
};

struct robot{
    int polynum = 0;
    vector <polygon> polys;
    config initcg;
    config goalcg;
    vector<point> cps;
};

int step = 200;
vector <obstacle> obstacles;
vector <robot> robots;

void search(){
    ofstream fout(OUTPUT_DIR);
    fout << robots.size() << endl;

    for (int i=0; i<robots.size(); i++){
        fout << step << endl;
        double x = robots[i].initcg.x, y = robots[i].initcg.y, theta = robots[i].initcg.theta;
        for(int j=0; j<step; j++){
            x += (robots[i].goalcg.x - robots[i].initcg.x)/ (double)step;
            y += (robots[i].goalcg.y -  robots[i].initcg.y)/ (double)step;
            theta += (robots[i].goalcg.theta  - robots[i].initcg.theta) / (double)step;
            fout << x << " " << y << " " << theta << endl;
        }
    }
}

int main(){
    
    ifstream fin(INPUT_DIR);
    
    int n;
    fin >> n;
    while(n--){
        obstacle tmpob;
        int polyn;
        fin >> polyn;
        tmpob.polynum = polyn;
        while(polyn--){
            int verticen;
            fin >> verticen;
            polygon tmppy;
            while(verticen--){
                double x, y;
                fin >> x >> y;
                tmppy.vertices.push_back({x, y});
            }
            tmpob.polys.push_back(tmppy);
        }
        fin >> tmpob.cg.x >> tmpob.cg.y >> tmpob.cg.theta;
        obstacles.push_back(tmpob);
    }

    
    fin >> n;
    while(n--){
        robot tmprb;
        int polyn;
        fin >> polyn;
        tmprb.polynum = polyn;
        while(polyn--){
            int verticen;
            fin >> verticen;
            polygon tmppy;
            while(verticen--){
                double x, y;
                fin >> x >> y;
                tmppy.vertices.push_back({x, y});
            }
            tmprb.polys.push_back(tmppy);
        }
        fin >> tmprb.initcg.x >> tmprb.initcg.y >> tmprb.initcg.theta;
        fin >> tmprb.goalcg.x >> tmprb.goalcg.y >> tmprb.goalcg.theta;
        int cpn;
        fin >> cpn;
        while(cpn--){
            double x, y;
            fin >> x >> y;
            tmprb.cps.push_back({x, y});
        }
        robots.push_back(tmprb);
    }


    search();


    /*fout << "2" << endl;
    fout << speed << endl;

    double x = 64.000000, y = 64.000000, theta = 90.000000;
    for(int i=0; i<speed; i++){
        x += (80.0 - 64.0)/ (double)speed;
        y += (80.0 - 64.0)/ (double)speed;
        theta -= 90.0 / (double)speed;
        fout << x << " " << y << " " << theta << endl;
    }
    //80.000000 80.000000 0.000000

    fout << speed << endl;
    x = 20.000000, y = 20.000000, theta = 90.000000;
    for(int i=0; i<speed; i++){
        x += (30.0 - 20.0)/ (double)speed;
        y += (100.0 - 20.0)/ (double)speed;
        theta -= 90.0 / (double)speed;
        fout << x << " " << y << " " << theta << endl;
    
    }
    //30.000000 100.000000 0.000000
    */

}

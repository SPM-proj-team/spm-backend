import http from 'k6/http';
import { sleep, check } from 'k6';
import { textSummary } from 'https://jslib.k6.io/k6-summary/0.0.1/index.js';

export const options = {
  stages: [
    { duration: '2s', target: 60 }, // simulate ramp-up of traffic from 1 to 60 users.
    { duration: '5s', target: 60 }, // stay at 60 users
    { duration: '2s', target: 100 }, // ramp-up to 100 users (peak hour starts)
    { duration: '1s', target: 100 }, // stay at 100 users for short amount of time (peak hour)
    { duration: '2s', target: 60 }, // ramp-down to 60 users (peak hour ends)
    { duration: '5s', target: 60 }, // continue at 60
    { duration: '2s', target: 0 }, // ramp-down to 0 users
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(90)<5000'], // 95 percent of response times must be below 5s
  },
};

export default function () {
  const headers = { 'Content-Type': 'application/json' };
  const getAccessRoles = http.get('http://127.0.0.1:5000/accessrole');
  check(getAccessRoles, {
    'is status 200': (r) => r.status === 200
  });
  const getCourses = http.get('http://127.0.0.1:5000/courses');
  check(getCourses, {
    'is status 200': (r) => r.status === 200
  });
  const updateCoursesData = { 
    "Course_ID": "COR001",
    "Skills": [3] 
  };
  const updateCourses = http.put('http://127.0.0.1:5000/courses', JSON.stringify(updateCoursesData), { headers: headers })
  check(updateCourses, {
    'is status 200': (r) => r.status === 200
  });
  const getLJData = { 
    "Staff_ID": "1"
  };
  const getLJ = http.post('http://127.0.0.1:5000/learning_journey', JSON.stringify(getLJData), {headers: headers});
  check(getLJ, {
    'is status 200': (r) => r.status === 200
  });
  // const createLJData = { 
  //   "Staff_ID": 1,
  //   "Learning_Journey": {
  //       "Courses": [
  //           {
  //               "Course_ID": "COR001"
  //           }
  //       ],
  //       "Description": "create",
  //       "Learning_Journey_Name": "Learning Journey for Full Stack Developer",
  //       "Role": {
  //           "Department": "Operations",
  //           "Description": "Slavery is no go. Please promote me",
  //           "Job_ID": 1,
  //           "Job_Role": "Operation Slave",
  //           "Job_Title": "Staff"
  //       },
  //       "Staff_ID": 1
  //   }
  // };
  // const createLJ = http.post('http://127.0.0.1:5000/learning_journey/create', JSON.stringify(createLJData), {headers: headers})
  // check(createLJ, {
  //   'is status 200': (r) => r.status === 200
  // });
  const updateLJData = { 
      "Staff_ID": 1,
      "Learning_Journey": {"Learning_Journey_ID": 1,
      "Courses": [{"Course_Category": "Core",
                  "Course_Desc": "This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking",
                  "Course_ID": "COR001",
                  "Course_Name": "Systems Thinking and Design",
                  "Course_Status": "Active",
                  "Course_Type": "Internal"},
                  {"Course_Category": "Core",
                  "Course_Desc": "Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics",
                  "Course_ID": "COR002",
                  "Course_Name": "Lean Six Sigma Green Belt Certification",
                  "Course_Status": "Active",
                  "Course_Type": "Internal"}],
      "Description": "test",
      "Learning_Journey_Name": "Learning Journey for Full Stack",
      "Role": {"Department": "C-suite",
              "Description": "lorem ipsum",
              "Job_ID": 1,
              "Job_Role": "CEO",
              "Job_Title": "The big boss"}}
  };
  const updateLJ = http.put('http://127.0.0.1:5000/learning_journey/1', JSON.stringify(updateLJData), { headers: headers })
  check(updateLJ, {
    'is status 200': (r) => r.status === 200
  });
//   const deleteLJData = {
//     "Staff_ID": 1
//   }
//   const deleteLJ = http.del('http://127.0.0.1:5000/learning_journey/1', JSON.stringify(deleteLJData), { headers: headers })
//   check(deleteLJ, {
//     'is status 200': (r) => r.status === 200
//   });
  const getJobRoles = http.get('http://127.0.0.1:5000/roles');
  check(getJobRoles, {
    'is status 200': (r) => r.status === 200
  });
  const getSkills = http.get('http://127.0.0.1:5000/skills');
  check(getSkills, {
    'is status 200': (r) => r.status === 200
  });
  const getStaff = http.get('http://127.0.0.1:5000/staff');
  check(getStaff, {
    'is status 200': (r) => r.status === 200
  });
  sleep(1);
}

export function handleSummary(data) {
  console.log('Finished executing performance tests');

  return {
    'stdout': textSummary(data, { indent: ' ', enableColors: true }), // Show the text summary to stdout...
    'summary.json': JSON.stringify(data), // and a JSON with all the details...
  };
}
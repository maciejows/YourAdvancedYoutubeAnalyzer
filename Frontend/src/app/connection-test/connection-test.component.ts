import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-connection-test',
  templateUrl: './connection-test.component.html',
  styleUrls: ['./connection-test.component.scss']
})
export class ConnectionTestComponent {

  data = { id: 2, name: 'InsertedWithPOST'};

  constructor(private _http: HttpClient) { }
  
  getMethod(){
    this._http.get('http://172.16.100.73:5000/test')
    .subscribe( (response) => console.log(response) );
  }

  postMethod(){
    const headers = new HttpHeaders()
    .set('Content-Type', 'application/json');

    this._http.post('http://172.16.100.73:5000/test', JSON.stringify(this.data), {headers: headers})
    .subscribe( (response) => console.log(response) );
  }

  putMethod(){
    const data = { id: 2, name: 'ChangedByPut'};

    const headers = new HttpHeaders()
    .set('Content-Type', 'application/json');

    this._http.put('http://172.16.100.73:5000/test', JSON.stringify(data), {headers: headers})
    .subscribe( (response) => console.log(response) );
  }

}
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Data } from '../data';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  getData(videoUrl: string): Observable<Data> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
      }),
      params: {url: videoUrl}
    };

    return this.http.get<Data>('http://127.0.0.1:5034/vid', httpOptions);
  }

}

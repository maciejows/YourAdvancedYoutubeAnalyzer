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
    const videoId = videoUrl.split("watch?v=");
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
      }),
      params: {url: videoId[1]}
    };
    return this.http.get<Data>('http://127.0.0.1:5034/vid', httpOptions);
  }

  getHistogram(videoUrl: string): Observable<string>{
    const videoId = videoUrl.split("watch?v=");
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
      }),
      params: {url: videoId[1]}
    };
    return this.http.get<string>('http://127.0.0.1:5034/hist', httpOptions);
  }

  getComments(videoUrl: string): Observable<any>{
    const videoId = videoUrl.split("watch?v=");
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type':  'application/json',
      }),
      params: {url: videoId[1]}
    };
    return this.http.get('http://127.0.0.1:5034/comm', httpOptions);
  }
   
  getTopVideosData(): Observable<any>{
    return this.http.get('http://127.0.0.1:5034/top');
  }

}

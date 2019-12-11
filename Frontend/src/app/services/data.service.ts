import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';
import { Data } from '../data';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  // TODO http://localhost:4200/?# ???????
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

}

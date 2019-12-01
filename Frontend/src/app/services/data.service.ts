import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  getData(videoUrl: string): any{
    return this.http.get('http://127.0.0.1:5034/vid', {params: {url: videoUrl}});
  }

}

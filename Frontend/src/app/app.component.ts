import { Component} from '@angular/core';
import { Data } from './data';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  data: Data;
  searched: boolean;
  
  getData(event: Data){
    this.data = event;
    console.log("Got data in app.component");
  }

  isSearching(event: boolean){
    this.searched = event;
  }

}

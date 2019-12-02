import { Component} from '@angular/core';
import { Data } from './data';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  data: any;
  searched: boolean;
  
  getData(event: any){
    this.data = event;
    console.log(`Root here, got data: ${event}`)
  }

  isSearching(event: boolean){
    this.searched = event;
  }

}

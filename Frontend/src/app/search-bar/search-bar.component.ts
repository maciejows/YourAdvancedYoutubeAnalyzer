import { Component, EventEmitter, Output} from '@angular/core';
import { DataService } from '../services/data.service';
import { Data } from '../data';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent{

  @Output() data = new EventEmitter<any>();
  @Output() searched = new EventEmitter<boolean>();
 

  constructor(private dataService: DataService) { }


  //TODO Need to unpack JSON
  // TODO http://localhost:4200/?# ???????
  getData(url): void{
    this.searched.emit(true);
    this.data.emit(null);
    this.dataService.getData(url)
    .subscribe( data => {
      console.log(data);
      this.data.emit(data.id as Data);
    });
  }

}

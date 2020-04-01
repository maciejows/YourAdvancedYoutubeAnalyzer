import { Component, EventEmitter, Output} from '@angular/core';
import { DataService } from '../services/data.service';
import { Data } from '../data';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent{

  @Output() data = new EventEmitter<Data>();
  @Output() histogramUrl = new EventEmitter();
  @Output() searched = new EventEmitter<boolean>();

  constructor(private dataService: DataService) { }

  getData(url: string): void {
    this.searched.emit(true);
    this.data.emit(null);
    
    this.dataService.getData(url)
    .subscribe( (data) => {
      console.log("Emiting data in search.component");
     this.data.emit(data);
    });
  }

  getHistogram(url: string): void{
    this.dataService.getHistogram(url)
    .subscribe( (data) => {
      console.log(`Emiting histogram in search.component ${data}`);
      setTimeout( ()=> this.histogramUrl.emit(data), 4000);
    });
  }

}

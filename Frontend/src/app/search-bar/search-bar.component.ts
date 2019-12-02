import { Component, EventEmitter, Output} from '@angular/core';
import { DataService } from '../services/data.service';
import { Data } from '../data';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-search-bar',
  templateUrl: './search-bar.component.html',
  styleUrls: ['./search-bar.component.scss']
})
export class SearchBarComponent{

  @Output() data = new EventEmitter<Data>();
  @Output() searched = new EventEmitter<boolean>();

  constructor(private dataService: DataService) { }

  getData(url): void {
    this.searched.emit(true);
    this.data.emit(null);
    
    this.dataService.getData(url)
    .subscribe( (data) => {
      this.data.emit(data);
    });
  }

}

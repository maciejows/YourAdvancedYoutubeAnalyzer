import { Component, Input} from '@angular/core';
import { Data } from '../data';

@Component({
  selector: 'app-data-display',
  templateUrl: './data-display.component.html',
  styleUrls: ['./data-display.component.scss']
})
export class DataDisplayComponent{

  @Input() data: Data;
  @Input() searched: boolean;
  constructor() { }

}

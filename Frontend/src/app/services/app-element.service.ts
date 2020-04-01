import { Injectable } from '@angular/core';

interface DomElementReference {
  [key: string] : HTMLElement;
}

@Injectable({
  providedIn: 'root'
})

export class AppElementService {
  public elements: DomElementReference = {};

  constructor() { }
}
